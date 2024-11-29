import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching the page:[/bold red] {e}")
        return None

def display_page(content):
    console.clear()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Website Raw Content", style="dim", width=80)
    table.add_row(content)
    console.print(table)

def main():
    console.print(Text("Pyscrape App By RK!", style="bold green"), justify="center")
    console.print(Text("Enter URL Of The Website!", style="bold cyan"), justify="center")
    
    url = console.input("[bold yellow]URL: [/bold yellow]").strip()
    if not url.startswith("http"):
        url = "http://" + url  # Add http if missing
    
    content = fetch_page(url)
    if content:
        display_page(content)
      
    console.print("\n[bold cyan]Web Scraper Terminal Base App By (RK) From RK Studio![/bold cyan]")
    console.print("\n[bold cyan]App Closed. Goodbye![/bold cyan]")

if __name__ == "__main__":
    main()
