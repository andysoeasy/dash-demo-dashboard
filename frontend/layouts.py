from dash import html, dcc
import dash_bootstrap_components as dbc
from config import COMPANIES, MONTH, YEARS, WEEKS, QUARTERS, COLORS_BASE_THEME, STRATEGIES
from utils import create_stat_card

page_content = html.Div(id = 'page-content')

# ------------------- Страница "Анализ стационарности" --------------------

stationaty_analysis_page = dbc.Container([
    html.H1("Анализ стационарности", className="my-4", style = {'color': COLORS_BASE_THEME['main_title']}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H4("Фильтры")),
                dbc.CardBody([
                    html.H5("Период", className="mb-2"),

                    dbc.Row([
                        dbc.Col(
                            dcc.Dropdown(
                                options = [{'label': year, 'value': year} for year in YEARS],
                                value= min(YEARS),
                                id='year-dropdown-page-1'
                            )
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                options = [{'label': quarter, 'value': i + 1} for i, quarter in enumerate(QUARTERS)], 
                                id='quarter-dropdown-page-1'
                            )
                        ),
                    ], className="mb-3"),

                    dbc.Row([
                        dbc.Col(
                            dcc.Dropdown(
                                options = [{'label': month, 'value': i + 1} for i, month in enumerate(MONTH)],
                                id='month-dropdown-page-1'
                            )
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                options = [{'label': week, 'value': week} for week in WEEKS], 
                                id='week-dropdown-page-1'
                            )
                        ),
                    ], className="mb-3"),

                    html.Hr(),

                    html.H5("Окно", className="mb-2"),
                    dcc.Slider(
                        min=1, max=30, step=1, value=7,
                        marks={1: '1', 7: '7', 14: '14', 30: '30'},
                        id='window-slider-page-1'
                    ),

                    html.Hr(),

                    html.H5("Акции", className="mb-2"),
                    dcc.Dropdown(
                        options = [{'label': company, 'value': company} for company in COMPANIES],
                        value = [COMPANIES[0]],
                        id = 'companies-dropdown-page-1',
                        multi = True,
                    ),
                ])
            ], className="shadow-sm mb-4"),

            dbc.Card([
                dbc.CardHeader(html.H4("Справка")),
                dbc.CardBody([
                    html.P('Здесь использованы данные площадки Yahoo!Finance. Период сбора информации - последние 2 года, включая начало мая 2026 года.')
                ])
            ], className="shadow-sm")
        ], width=2),

        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='main-chart-page-1')
                        ])
                    ], className="shadow-sm h-100")
                ], width=7),

                dbc.Col([
                    html.Div([
                        dbc.Row([
                            dbc.Col(id = 'adf', width = 4),
                            dbc.Col(id = 'kpss-trend', width = 4),
                            dbc.Col(id = 'kpss-level', width = 4)
                        ], className = 'flex-fill'),
                        dbc.Row([
                            dbc.Col(create_stat_card("ADF", "adf-value"), width=4),
                            dbc.Col(create_stat_card("KPSS (тренд)", "trend-value"), width=4),
                            dbc.Col(create_stat_card("KPSS (уровень)", "level-value"), width=4),
                        ], className="my-2 flex-fill"),
                        dbc.Row([
                            dbc.Col(create_stat_card("p-value", "adf-pvalue"), width=4),
                            dbc.Col(create_stat_card("p-value", "trend-pvalue"), width=4),
                            dbc.Col(create_stat_card("p-value", "level-pvalue"), width=4),
                        ], className="mb-2 flex-fill"),
                        dbc.Row([
                            dbc.Col(create_stat_card("5%", "adf-5pct"), width=4),
                            dbc.Col(create_stat_card("5%", "trend-5pct"), width=4),
                            dbc.Col(create_stat_card("5%", "level-5pct"), width=4),
                        ], className = 'flex-fill'),
                    ], className = 'd-flex flex-column h-100 justify-content-between')
                ], width=5, className = ''),
            ], className="mb-4 align-items-stretch"),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='returns-chart-page-1')
                        ])
                    ], className="shadow-sm")
                ], width=6),

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id='volatility-chart-page-1')
                        ])
                    ], className="shadow-sm")
                ], width=6),
            ])
        ], width=10)
    ])
], fluid=True, style = {'backgroundColor': COLORS_BASE_THEME['background_chart']})


# Страница Анализ стратегий

strategy_analysis_page = dbc.Container(
    [
        html.H1("Анализ стратегий", className="my-4", style = {'color': COLORS_BASE_THEME['main_title']}),

        dbc.Row(
            [
                dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Фильтры")),
                            dbc.CardBody(
                                [
                                    html.H5("Период", className="mb-2"),

                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    options = [{'label': year, 'value': year} for year in YEARS],
                                                    value= min(YEARS),
                                                    id='year-dropdown-page-2'
                                                )
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    options = [{'label': quarter, 'value': i + 1} for i, quarter in enumerate(QUARTERS)], 
                                                    id='quarter-dropdown-page-2'
                                                )
                                            ),
                                        ], 
                                        className="mb-3"
                                    ),

                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    options = [{'label': month, 'value': i + 1} for i, month in enumerate(MONTH)],
                                                    id='month-dropdown-page-2'
                                                )
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    options = [{'label': week, 'value': week} for week in WEEKS], 
                                                    id='week-dropdown-page-2'
                                                )
                                            ),
                                        ],
                                        className="mb-3"
                                    ),

                                    html.Hr(),

                                    html.H5("Long Window", className="mb-2"),
                                    dcc.Slider(
                                        min=28, max=252, step=1, value=28,
                                        marks={28: '28', 56: '56', 126: '126', 252: '252'},
                                        id='long-window-slider-page-2'
                                    ),

                                    html.Hr(),

                                    html.H5("Short Window", className="mb-2"),
                                    dcc.Slider(
                                        min=1, max=14, step=1, value=7,
                                        marks={1: '1', 7: '7', 14: '14'},
                                        id='short-window-slider-page-2'
                                    ),
                                    
                                    html.Hr(),

                                    html.H5("Entry Threshold", className = 'mb-2'),
                                    dcc.Input(
                                        min=0.1, max=5.0,
                                        type='number',
                                        debounce=True,
                                        value = 1.57,
                                        placeholder='Введите значение',
                                        id = 'entry-threshold-input-page-2'
                                    ),

                                    html.Hr(),

                                    html.H5("Exit Threshold", className = 'mb-2'),
                                    dcc.Input(
                                        min=0.1, max=5.0,
                                        type='number',
                                        debounce=True,
                                        value = 0.25,
                                        placeholder='Введите значение',
                                        id = 'exit-threshold-input-page-2'
                                    ),

                                    html.Hr(),

                                    html.H5("Акции", className="mb-2"),
                                    dcc.Dropdown(
                                        options = [{'label': company, 'value': company} for company in COMPANIES],
                                        value = COMPANIES[0],
                                        id = 'companies-dropdown-page-2',
                                    ),

                                    html.Hr(),

                                    html.H5("Стратегии", className="mb-2"),
                                    dcc.Dropdown(
                                        options = [{'label': strategy, 'value': strategy} for strategy in STRATEGIES],
                                        value = STRATEGIES[0],
                                        id = 'strategies-dropdown-page-2',
                                    ),
                                ]
                            )
                        ], 
                        className="shadow-sm mb-4"
                    ),

                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Справка")),
                            dbc.CardBody(
                                html.P('Здесь использованы данные площадки Yahoo!Finance. Период сбора информации - последние 2 года, включая начало мая 2026 года.')
                            )
                        ], 
                        className="shadow-sm"
                    )
                ],
                width = 2
            ),
                dbc.Col(                    
                    [
                        dbc.Row(
                            [
                                dbc.Col(        
                                    [
                                        dbc.Row(
                                            dbc.Col(
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        dcc.Graph(id = 'strategies-page-2')
                                                    ),
                                                    className = 'shadow-sm mb-4'
                                                ),
                                                width = 12
                                            )
                                        ),
                                        dbc.Row(
                                            dbc.Col(
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        dcc.Graph(id = 'z-score-intervals-page-2')
                                                    ),
                                                    className = 'shadow-sm mb-4'
                                                ),
                                                width = 12
                                            )
                                        ),
                                    ],
                                    width = 7
                                ),
                                dbc.Col(              
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dbc.Card(
                                                        [
                                                            dbc.CardHeader(
                                                                html.H4('Метрики бенчмарка')
                                                            ),
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        create_stat_card('Общая доходность', 'all-returns-benchmark'),
                                                                        className = 'mb-2'
                                                                    ),
                                                                    dbc.Row(
                                                                        create_stat_card('Sharpe Ratio', 'sharpe-ratio-benchmark'),
                                                                        className = 'mb-2'
                                                                    ),
                                                                    dbc.Row(
                                                                        create_stat_card('Просадки', 'drawdown-benchmark'),
                                                                        className = 'mb-2'
                                                                    ),
                                                                    dbc.Row(
                                                                        create_stat_card('Количество сделок', 'num-trades-benchmark')
                                                                    )
                                                                ]
                                                            )
                                                        ],
                                                        className = 'shadow-sm mb-4'
                                                    ),
                                                    width = 6
                                                ),
                                                dbc.Col(
                                                    dbc.Card(
                                                        [
                                                            dbc.CardHeader(
                                                                html.H4('Метрики стратегии')
                                                            ),
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        create_stat_card('Общая доходность', 'all-returns-strategy'),
                                                                        className = 'mb-2'
                                                                    ),
                                                                    dbc.Row(
                                                                        create_stat_card('Sharpe Ratio', 'sharpe-ratio-strategy'),
                                                                        className = 'mb-2'
                                                                    ),
                                                                    dbc.Row(
                                                                        create_stat_card('Просадки', 'drawdown-strategy'),
                                                                        className = 'mb-2'
                                                                    ),
                                                                    dbc.Row(
                                                                        create_stat_card('Количество сделок', 'num-trades-strategy')
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    width = 6
                                                ),
                                            ]
                                        ),
                                        dbc.Row(
                                            dbc.Col(
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        dcc.Graph(id = 'main-chart-page-2')
                                                    ),
                                                    className = 'shadow-sm mb-4'
                                                ),
                                                width = 12
                                            )
                                        ),
                                    ],
                                    width = 5
                                )
                            ]
                        ),
                    ],
                    width = 10
                )
            ]
        ),
    ],
    fluid = True,
    style = {'backgroundColor': COLORS_BASE_THEME['background_chart']}
)