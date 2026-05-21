import dash_bootstrap_components as dbc


from config import COLORS_BASE_THEME

navbar = dbc.NavbarSimple(
    [
        dbc.NavItem(
            dbc.NavLink(
                'Анализ стационарности',
                href = '/page-1'
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                'Анализ стратегий',
                href = '/page-2'
            )
        )
    ],
    brand = 'Простой многостраничный дашборд',
    brand_href = '/',
    color = COLORS_BASE_THEME['main_title'],
    className = 'mb-4'
)

