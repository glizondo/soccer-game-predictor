import matches
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

games = pd.read_csv("../liga.csv", index_col=0)

games["Date"] = pd.to_datetime(games["Date"])
print(games["Date"])
print(games.dtypes)

# X = df[["HomeTeam", "AwayTeam", "HTHG", "HTAG", "HTR", "HS", "AS", "HST", "AST", "HF", "AF", "HC", "AC", "HY",
#         "AY", "HR", "AR", "B365H", "B365D", "B365A", "BWH", "BWD", "BWA", "IWH", "IWD", "IWA", "LBH", "LBD", "LBA",
#         "PSH", "PSD", "PSA", "WHH", "WHD", "WHA", "SJH", "SJD", "SJA", "VCH", "VCD", "VCA", "Bb1X2", "BbMxH", "BbAvH",
#         "BbMxD", "BbAvD", "BbMxA", "BbAvA", "BbOU", "BbMx>2.5", "BbAv>2.5", "BbMx<2.5", "BbAv<2.5", "BbAH", "BbAHh",
#         "BbMxAHH", "BbAvAHH", "BbMxAHA", "BbAvAHA", "PSCH", "PSCD", "PSCA"]]
# Y = df[["FTHG", "FTAG"]]
#
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)
# model = LinearRegression()
# model.fit(X_train, Y_train)
#
# joblib.dump(model, 'liga_model.pkl')
#
# print("Model training results:")
# mse_train = mean_absolute_error(Y_train, model.predict(X_train))
# print(f" - Training Set Error: {mse_train}")
#
# mse_test = mean_absolute_error(Y_test, model.predict(X_test))
# print(f" - Test Set Error: {mse_test}")