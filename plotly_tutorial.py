import plotly.express as px
import pandas as pd

days = ["Monday", "Tuesday", "Wednesday"]
sleep_hours = [8, 9, 7]

fig = px.bar(
  x = days, 
  y = sleep_hours, 
  title = "Hours of sleep"
)
fig.show()

sleep = pd.DataFrame({
    "day": days,
    "sleep_hours": sleep_hours
})

fig = px.bar(
    data_frame=sleep,
    x = "day", y = "sleep_hours",
    title = "Sleep per day"
)