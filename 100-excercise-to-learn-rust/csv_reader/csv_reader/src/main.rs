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

fn calculate_sma(data: &[Ohlc], period: usize) -> Vec<f64> {
    let mut sma = Vec::with_capacity(data.len());
    
    // Initial values before we have enough data
    for _ in 0..period - 1 {
        sma.push(0.0);
    }

    // Calculate SMA for each window
    for i in period - 1..data.len() {
        let window = &data[i - (period - 1)..=i];
        let avg = window.iter().map(|x| x.close).sum::<f64>() / period as f64;
        sma.push(avg);
    }

    sma
}

fn main() -> Result<()> {
    let data = load_ohlc_data("data.csv")?;
    let sma = calculate_sma(&data, 3); // 3-period SMA
    
    println!("Loaded {} records", data.len());
    for (record, sma_val) in data.iter().zip(sma.iter()) {
        println!("Date: {}, Close: {}, SMA: {}", record.datetime, record.close, sma_val);
    }
    Ok(())
}
