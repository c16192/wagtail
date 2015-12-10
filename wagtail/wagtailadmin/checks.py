import os

from django.core.checks import Warning, register


def has_css_installed():
    wagtail_adm_css = os.path.join(os.path.dirname(__file__), 'css', 'normalize.css')
    succeeded = True

    try:
        open(wagtail_adm_css, 'r')
    except (IOError):
        succeeded = False

    return succeeded


@register()
def npm_install_check(app_configs, **kwargs):
    errors = []
    # ... your check logic here
    if not has_css_installed():
        errors.append(
            Warning(
                'css file cannot be found in correct directory.',
                hint="Check that the 'npm' is installed."
            )
        )
    return errors
