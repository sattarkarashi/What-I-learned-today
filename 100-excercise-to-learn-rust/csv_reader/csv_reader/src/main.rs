use serde::Deserialize;
use chrono::NaiveDate;
use anyhow::Result;

#[derive(Debug, Deserialize)]
struct Ohlc {
    #[serde(with = "my_date_format")]
    datetime: NaiveDate,
    open: f64,
    high: f64,
    low: f64,
    close: f64,
}

// Custom date format for CSV deserialization
mod my_date_format {
    use chrono::NaiveDate;
    use serde::{self, Deserialize, Deserializer};

    const FORMAT: &str = "%Y-%m-%d %H:%M:%S";

    pub fn deserialize<'de, D>(deserializer: D) -> Result<NaiveDate, D::Error>
    where
        D: Deserializer<'de>,
    {
        let s = String::deserialize(deserializer)?;
        NaiveDate::parse_from_str(&s, FORMAT).map_err(serde::de::Error::custom)
    }
}

fn load_ohlc_data(file_path: &str) -> Result<Vec<Ohlc>> {
    let mut rdr = csv::Reader::from_path(file_path)?;
    let mut data = Vec::new();

    for result in rdr.deserialize() {
        let record: Ohlc = result?;
        data.push(record);
    }

    Ok(data)
}

fn main() -> Result<()> {
    let data = load_ohlc_data("data.csv")?;
    println!("Loaded {} records", data.len());
    for record in data.iter().take(5) {
        println!("{:?}", record);
    }
    Ok(())
}
