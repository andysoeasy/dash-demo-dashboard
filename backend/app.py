import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    name = 'StudyExampleDashboard',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

app.title = 'ExampleTSAnalyticsDashboard'

app.config.suppress_callback_exceptions = True