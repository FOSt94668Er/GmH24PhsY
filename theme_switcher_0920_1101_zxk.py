# 代码生成时间: 2025-09-20 11:01:45
import pandas as pd

"""
Theme Switcher

This script allows the user to switch between predefined themes for a data table.
It uses pandas to manipulate the DataFrame and apply the specified theme.
"""

# Define custom themes for the DataFrame
THEMES = {
    "default": {
        "font_color": "black",
        "background_color": "white"
    },
    "dark": {
        "font_color": "white",
        "background_color": "#333333"  # Dark charcoal color
    }
}

# Define a function to apply the theme to a DataFrame
def apply_theme(df, theme_name):
    """
    Apply the specified theme to the DataFrame.
    
    Parameters:
    df (pd.DataFrame): DataFrame to apply the theme to.
    theme_name (str): Name of the theme to apply.
    
    Raises:
    ValueError: If the theme name is not found.
    """
    theme = THEMES.get(theme_name)
    if theme is None:
        raise ValueError(f"Theme '{theme_name}' not found.")
    
    # Apply the theme to the DataFrame
    df.style.set_properties(**theme)
    return df

# Example usage
if __name__ == '__main__':
    # Create a sample DataFrame
    data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
    df = pd.DataFrame(data)
    
    try:
        # Apply the default theme
        df_with_theme = apply_theme(df, "default\)
        print(df_with_theme)

        # Apply the dark theme
        df_with_theme = apply_theme(df, "dark\)
        print(df_with_theme)

    except ValueError as e:
        print(e)