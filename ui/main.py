import flet
from flet import Page, Tab, Tabs, Text, Column, Container


def main(page: Page):
    page.title = "EduIntel - Tomball High School Academic Dashboard"
    page.window_width = 800
    page.window_height = 600

    page.theme_mode = "light"
    text_style = {"color": "#000"}  # default black text

    home_content = Column([
        Text("Welcome to EduIntel!", size=24, weight="bold", **text_style),
        Text("Your personalized academic dashboard.", **text_style)
    ])

    classes_content = Column([
        Text("Classes Overview", size=24, weight="bold", **text_style),
        Text("Here you will see your current classes and grades.", **text_style)
    ])

    gpa_content = Column([
        Text("GPA Calculator & Projection", size=24, weight="bold", **text_style),
        Text("Calculate and forecast your GPA here.", **text_style)
    ])

    norman_content = Column([
        Text("Norman - Your AI Counselor", size=24, weight="bold", **text_style),
        Text("Ask Norman for help with course selections and academic advice.", **text_style)
    ])

    analytics_content = Column([
        Text("Academic Analytics", size=24, weight="bold", **text_style),
        Text("Insights and trends about your academic performance.", **text_style)
    ])

    tabs = Tabs(
        selected_index=0,
        tabs=[
            Tab(text="Home", content=Container(content=home_content, padding=20)),
            Tab(text="Classes", content=Container(content=classes_content, padding=20)),
            Tab(text="GPA", content=Container(content=gpa_content, padding=20)),
            Tab(text="Norman", content=Container(content=norman_content, padding=20)),
            Tab(text="Analytics", content=Container(content=analytics_content, padding=20)),
        ],
        expand=1,
    )

    page.add(Container(content=tabs, bgcolor="#fff", padding=0))


if __name__ == "__main__":
    flet.app(target=main)
