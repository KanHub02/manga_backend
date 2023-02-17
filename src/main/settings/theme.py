JAZZMIN_SETTINGS = {
    "site_title": "Manga TT for Geeks",
    "site_header": "Манга",
    "site_logo_classes": "img-circle",
    "site_icon": '/assets/icons/admin_logo.svg',
    "welcome_sign": "Добро пожаловать в панель администратора сайта Манга!",
    "copyright": "GeekStudio(Usmanov Kanat)",
    "search_model": "auth.User",
    "user_avatar": 'None',
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    "usermenu_links": [
        {
            "model": "auth.user",
        },
    ],
    "order_with_respect_to": [
        # apps
        "informations",
        "announcements",
        "decree",
        "vote",
        "auth",
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "language_chooser": True,
    "hide_apps": [],
    "hide_models": [],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "blog": "fas fa-book",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-thumbtack",
    "related_modal_active": True,
    "custom_css": "/common/style.css",
    "custom_js": None,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "icons": {
        "announcements.Vacancy": "fas fa-clipboard-check",
        "announcements.Conferences": "fas fa-folder",
        "announcements.UsefulInformation": "fas fa-newspaper",

        "decree.RegionalCity": "fa fa-location-arrow",
        "decree.Region": "fa fa-location-arrow",
        "decree.District": "fa fa-location-arrow",
        "decree.RuralManagement": "fas fa-map-pin",
        "decree.Resolutions": "fas fa-file-alt",

        "informations.CategoryOfQuestions": "fa fa-sort",
        "informations.Question": "fas fa-question",
        "informations.EmployeeCard": "fas fa-users",
        "informations.Act": "fas fa-gavel",
        "informations.ImageModel": "fas fa-image",
        "informations.News": "fa fa-newspaper",
        "informations.TestsCategory": "fas fa-list-ol",
        "informations.Tests": "fas fa-list-ol",

        "vote.CityDepartment": "fa fa-location-arrow",
        "vote.Region": "fa fa-location-arrow",
        "vote.District": "fa fa-location-arrow",
        "vote.RuralManagement": "fas fa-map-pin",
        "vote.Vote": "fas fa-vote-yea",
        "vote.Answer": "fas fa-list-alt",
        "vote.UserVoting": "fas fa-user-check",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}

