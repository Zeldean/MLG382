
# 🐍 Python Time Series Analysis Cheat Sheet

# 📦 Libraries to Import
# ----------------------
import pandas
import matplotlib.pyplot 
import seaborn
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet  # Optional: for advanced forecasting

# 📊 Load and Inspect Data
# ------------------------
df = pd.read_csv()
df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index('DATE', inplace=True)
df.rename(columns={'': ''}, inplace=True)

print(df.head())
print(df.describe())
print(df.info())

# 📈 Visualize the Time Series
# ----------------------------
plt.figure(figsize=(12,6))
plt.plot(df['Production'], label='')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.legend()
plt.show()

# 🔍 Decompose to See Trend & Seasonality
# ---------------------------------------
decomp = seasonal_decompose(, model='additive', period=12)
decomp.plot()
plt.show()

# 📅 Resample to Yearly Averages
# ------------------------------
yearly_avg = df.resample().mean()
print(yearly_avg.sort_values(by=, ascending=False))

# 📉 Build ARIMA Forecast
# -----------------------
model = ARIMA(df['Production'], order=(1,1,1))  # Change order based on AIC/BIC tuning
model_fit = model.fit()
forecast = model_fit.forecast(steps=12)

plt.figure(figsize=(10,6))
plt.plot(df['Production'], label='Actual')
plt.plot(forecast.index, forecast, label='Forecast', color='red')
plt.title('12-Month Forecast using ARIMA')
plt.legend()
plt.show()

# 🔮 (Optional) Forecast with Prophet
# -----------------------------------
# Prep data for Prophet
df_prophet = df.reset_index().rename(columns={'DATE': 'ds', 'Production': 'y'})
m = Prophet()
m.fit(df_prophet)
future = m.make_future_dataframe(periods=12, freq='M')
forecast = m.predict(future)

# Plot
fig = m.plot(forecast)


