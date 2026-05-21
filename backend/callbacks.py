from dash import Input, Output
import numpy as np

from .app import app
from .data import get_data, get_returns, get_volatility
from utils import (
    print_main_chart, 
    print_volatility_chart, 
    print_returns_chart, 
    create_dropdown_stat_cart, 
    get_statistic_coefs,
    mean_reversion,
    buy_and_hold,
    plot_prices,
    plot_z_score,
    plot_strategies
)

from frontend.layouts import stationaty_analysis_page, strategy_analysis_page

# ----------------- ===== Навигация между страницами ===== ----------------- #

@app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/page-1':
        return stationaty_analysis_page
    elif pathname == '/page-2':
        return strategy_analysis_page
    elif pathname == '/':
        return stationaty_analysis_page
    else:
        return stationaty_analysis_page

# ----------------- ===== Функциональность страницы Анализ стационарности ===== ----------------- #

@app.callback(
        [Output('quarter-dropdown-page-1', 'value'),
        Output('quarter-dropdown-page-1', 'disabled')],
        [Input('year-dropdown-page-1', 'value'),
        Input('month-dropdown-page-1', 'value')]
)
def disable_quarter(year, month):
    return (None, year is None) or (None, month is not None)

@app.callback(
        Output('month-dropdown-page-1', 'disabled'),
        Input('year-dropdown-page-1', 'value')
)
def disable_month(year):
    return year is None


@app.callback(
        Output('week-dropdown-page-1', 'disabled'),
        Input('month-dropdown-page-1', 'value')
)
def disable_week(month):
    return month is None

@app.callback(
        [
            Output('main-chart-page-1', 'figure'),
            Output('returns-chart-page-1', 'figure'),
            Output('volatility-chart-page-1', 'figure')
        ],
        [
            Input('companies-dropdown-page-1', 'value'),
            Input('year-dropdown-page-1', 'value'),
            Input('quarter-dropdown-page-1', 'value'),
            Input('month-dropdown-page-1', 'value'),
            Input('week-dropdown-page-1', 'value'),
            Input('window-slider-page-1', 'value')
        ]
)
def update_charts(companies, year, quarter, month, week, window):
    main_data = get_data(companies, year, quarter, month, week)
    returns_data = get_returns(precompute_data = main_data)
    volatility_data = get_volatility(precompute_data = returns_data, window = window)

    fig_main = print_main_chart(main_data)
    fig_returns = print_returns_chart(returns_data)
    fig_volatility = print_volatility_chart(volatility_data)

    return fig_main, fig_returns, fig_volatility

@app.callback(
        [
            Output('adf', 'children'),
            Output('kpss-trend', 'children'),
            Output('kpss-level' ,'children')
        ],
        [
            Input('companies-dropdown-page-1', 'value')
        ]
)
def create_dropdowns_stats(companies):
    return (
        create_dropdown_stat_cart(companies, 'adf-dropdown'),
        create_dropdown_stat_cart(companies, 'kpss-trend-dropdown'),
        create_dropdown_stat_cart(companies, 'kpss-level-dropdown')
    )


@app.callback(
        [
            Output('adf-value', 'children'),
            Output('adf-pvalue', 'children'),
            Output('adf-5pct' ,'children')
        ],
        [
            Input('adf-dropdown', 'value'),
            Input('year-dropdown-page-1', 'value'),
            Input('quarter-dropdown-page-1', 'value'),
            Input('month-dropdown-page-1', 'value'),
            Input('week-dropdown-page-1', 'value'),
        ]
)
def print_adf_stats(company, year, quarter, month, week):
    data = get_data([company], year, quarter, month, week)

    return get_statistic_coefs(data, type = 'adfuller')


@app.callback(
        [
            Output('trend-value', 'children'),
            Output('trend-pvalue', 'children'),
            Output('trend-5pct' ,'children')
        ],
        [
            Input('kpss-trend-dropdown', 'value'),
            Input('year-dropdown-page-1', 'value'),
            Input('quarter-dropdown-page-1', 'value'),
            Input('month-dropdown-page-1', 'value'),
            Input('week-dropdown-page-1', 'value'),
        ]
)
def print_kpss_trend_stats(company, year, quarter, month, week):
    data = get_data([company], year, quarter, month, week)

    return get_statistic_coefs(data, type = 'kpss_trend')


@app.callback(
        [
            Output('level-value', 'children'),
            Output('level-pvalue', 'children'),
            Output('level-5pct' ,'children')
        ],
        [
            Input('kpss-level-dropdown', 'value'),
            Input('year-dropdown-page-1', 'value'),
            Input('quarter-dropdown-page-1', 'value'),
            Input('month-dropdown-page-1', 'value'),
            Input('week-dropdown-page-1', 'value'),
        ]
)
def print_kpss_level_stats(company, year, quarter, month, week):
    data = get_data([company], year, quarter, month, week)

    return get_statistic_coefs(data, type = 'kpss_level')


# ----------------- ===== Функциональность страницы Анализ стратегий ===== ----------------- #
@app.callback(
        [Output('quarter-dropdown-page-2', 'value'),
        Output('quarter-dropdown-page-2', 'disabled')],
        [Input('year-dropdown-page-2', 'value'),
        Input('month-dropdown-page-2', 'value')]
)
def disable_quarter_page2(year, month):
    return (None, year is None) or (None, month is not None)

@app.callback(
        Output('month-dropdown-page-2', 'disabled'),
        Input('year-dropdown-page-2', 'value')
)
def disable_month_page2(year):
    return year is None


@app.callback(
        Output('week-dropdown-page-2', 'disabled'),
        Input('month-dropdown-page-2', 'value')
)
def disable_week_page2(month):
    return month is None


@app.callback(
        [
            Output('main-chart-page-2', 'figure'),
            Output('z-score-intervals-page-2', 'figure'),
            Output('strategies-page-2', 'figure'),

            Output('all-returns-benchmark', 'children'),
            Output('sharpe-ratio-benchmark', 'children'),
            Output('drawdown-benchmark', 'children'),
            Output('num-trades-benchmark', 'children'),

            Output('all-returns-strategy', 'children'),
            Output('sharpe-ratio-strategy', 'children'),
            Output('drawdown-strategy', 'children'),
            Output('num-trades-strategy', 'children'),
        ],
        [
            Input('companies-dropdown-page-2', 'value'),
            Input('year-dropdown-page-2', 'value'),
            Input('quarter-dropdown-page-2', 'value'),
            Input('month-dropdown-page-2', 'value'),
            Input('week-dropdown-page-2', 'value'),
            Input('entry-threshold-input-page-2', 'value'),
            Input('exit-threshold-input-page-2', 'value'),
            Input('long-window-slider-page-2', 'value'),
            Input('short-window-slider-page-2', 'value')
        ]
)
def update_charts_page_2(
    company,
    year,
    quarter,
    month,
    week,
    entry_threshold,
    exit_threshold,
    long_window,
    short_window
):
    data = get_data(
        [company],
        year,
        quarter,
        month,
        week
    )

    strat_names = {
        'Mean Reversion': mean_reversion
    }

    prices = data.squeeze()
    signals, metrics_straregy = strat_names['Mean Reversion'](
        prices,
        long = long_window,
        entry_threshold = entry_threshold,
        exit_threshold = exit_threshold
    )

    benchmark_strategy = prices / prices.iloc[0]
    metrics_benchmark = buy_and_hold(prices)

    mean_reversion_strat = (1 + signals['strategy_returns'].fillna(0)).cumprod()

    strategies = {
        'Buy&Hold': benchmark_strategy,
        'Mean-Reversion': mean_reversion_strat
    }

    prices_plot = plot_prices(
        signals,
        short_window,
        long_window,
        company
    )

    z_score_plot = plot_z_score(
        signals,
        entry_threshold,
        exit_threshold
    )

    strategy_plot = plot_strategies(
        signals,
        strategies
    )


    return (
        prices_plot,
        z_score_plot,
        strategy_plot,

        f'{metrics_benchmark['total_return'] * 100:.3f} %',
        f'{metrics_benchmark['sharpe_ratio']:.3f}',
        f'{metrics_benchmark['max_drawdown'] * 100:.3f} %',
        metrics_benchmark['num_trades'],

        f'{metrics_straregy['total_return'] * 100:.3f} %',
        f'{ metrics_straregy['sharpe_ratio']:.3f}',
        f'{metrics_straregy['max_drawdown'] * 100:.3f} %',
        metrics_straregy['num_trades'],
    )