"""
Proste przetwarzanie danych Excel.
Funkcje:
- load_excel(path=None): wczytuje plik Excel (domyślnie ./excel/data.xlsx)
- clean_dataframe(df): upraszcza nazwy kolumn, usuwa tylko-białe komórki
- summarize_df(df): zwraca DataFrame ze statystykami dla kolumn numerycznych i licznikami dla nienumerycznych
- save_summary(summary_df, out_path): zapisuje podsumowanie do CSV

Uruchomienie: python dzien4/dane.py
Jeśli brakuje pakietów, zainstaluj: pip install -r requirements.txt
"""
from pathlib import Path
from typing import Optional

try:
    import pandas as pd
except Exception:
    pd = None


def _default_excel_path() -> Path:
    return Path(__file__).parent / "excel" / "data.xlsx"


def load_excel(path: Optional[str] = None) -> "pd.DataFrame":
    """Wczytuje arkusz Excel do DataFrame. Jeśli brak pandas, rzuca ImportError z opisem.
    Jeśli path nie podano, używa domyślnej lokalizacji dzien4/excel/data.xlsx.
    """
    if pd is None:
        raise ImportError("Brakuje pakietu pandas lub nie można go załadować. Zainstaluj pandas oraz openpyxl.")

    p = Path(path) if path else _default_excel_path()
    if not p.exists():
        raise FileNotFoundError(f"Plik nie istnieje: {p}")

    # pandas automatycznie wykryje format; dla xlsx wymaga openpyxl
    df = pd.read_excel(p)
    return df


def clean_dataframe(df: "pd.DataFrame") -> "pd.DataFrame":
    """Proste czyszczenie:
    - usunięcie kolumn składających się tylko z NaN
    - obcięcie spacji w stringach
    - ujednolicenie nazw kolumn (lower, replace spacje -> _)
    """
    if df is None:
        raise ValueError("Przekaż DataFrame do czyszczenia")

    # usuń kolumny, które są w całości NaN
    df = df.dropna(axis=1, how="all")

    # obetnij spacje w kolumnach typu object
    for col in df.select_dtypes(include=[object]).columns:
        df[col] = df[col].astype(str).str.strip()
        # jeśli była pusta komórka -> 'nan' jako string, zamień z powrotem na NaN
        df[col] = df[col].replace({"nan": pd.NA, "None": pd.NA})

    # ujednolicenie nazw kolumn
    new_cols = {col: str(col).strip().lower().replace(" ", "_") for col in df.columns}
    df = df.rename(columns=new_cols)

    return df


def summarize_df(df: "pd.DataFrame") -> "pd.DataFrame":
    """Zwraca podsumowanie: dla kolumn numerycznych -> count/mean/std/min/max; dla nienumerycznych -> liczba unikalnych i liczba braków.
    Dodatkowo zwraca liczbę duplikatów w całym DataFrame.
    """
    if pd is None:
        raise ImportError("Brakuje pakietu pandas")
    if df is None:
        raise ValueError("Brak DataFrame do podsumowania")

    num = df.select_dtypes(include=["number"]).describe().T
    num = num[["count", "mean", "std", "min", "max"]]

    obj_cols = []
    for col in df.columns:
        if col not in num.index:
            obj_cols.append({
                "column": col,
                "n_unique": int(df[col].nunique(dropna=True)),
                "n_missing": int(df[col].isna().sum()),
                "dtype": str(df[col].dtype),
            })
    obj = pd.DataFrame(obj_cols).set_index("column") if obj_cols else pd.DataFrame()

    # Połącz podsumowanie: numeryczne + nienumeryczne (w pionie) i dodaj informację o duplikatach
    # Aby zachować czytelność, przygotujemy multiindexowy DataFrame
    parts = []
    if not num.empty:
        num = num.rename(columns={"count": "count", "mean": "mean", "std": "std", "min": "min", "max": "max"})
        parts.append(num)
    if not obj.empty:
        parts.append(obj)

    if parts:
        summary = pd.concat(parts, sort=False)
    else:
        summary = pd.DataFrame()

    # dodaj informację o duplikatach jako osobny wiersz
    dup_count = int(df.duplicated().sum())
    meta = pd.DataFrame({"info": [f"duplicates: {dup_count}", f"rows: {len(df)}"]}, index=["_meta_", "_meta_2_"])

    # Zwróć krotkę (summary, meta) dla elastyczności
    return summary, meta


def save_summary(summary_df: "pd.DataFrame", out_path: Optional[str] = None):
    out_dir = Path(__file__).parent / "excel"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (out_path if out_path else "wynik_dane_summary.csv")
    # jeśli tuple (summary, meta)
    if isinstance(summary_df, tuple):
        summary, meta = summary_df
        # zapisz oba jako oddzielne arkusze w Excel lub jako CSV-y. Proste: do jednego CSV z separatorami.
        with open(out, "w", encoding="utf-8", newline="") as f:
            f.write("# SUMMARY\n")
            if not summary.empty:
                summary.to_csv(f)
            else:
                f.write("(brak danych numerycznych ani obiektowych)\n")
            f.write("\n# META\n")
            meta.to_csv(f)
    else:
        summary_df.to_csv(out)
    return out


if __name__ == "__main__":
    print("Uruchamianie prostego przetwarzania danych Excel: dzien4/excel/data.xlsx")
    try:
        df = load_excel()
    except Exception as e:
        print("Błąd podczas wczytywania pliku:", e)
        print("Upewnij się, że plik istnieje i zainstalowano wymagane pakiety: pip install -r requirements.txt")
    else:
        print(f"Wczytano DataFrame: {df.shape[0]} wierszy x {df.shape[1]} kolumn")
        df = clean_dataframe(df)
        summary, meta = summarize_df(df)
        out = save_summary((summary, meta))
        print("Zapisano podsumowanie do:", out)

