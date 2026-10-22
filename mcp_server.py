from mcp.server.fastmcp import FastMCP

from siclone import clone_site

mcp = FastMCP("siclone")


@mcp.tool()
def clone_website(url: str, output_dir: str = "site_clone") -> dict:
    """Download a static website's HTML, CSS, JS, and images, and rewrite
    the HTML to reference the local copies so it works offline.

    Args:
        url: The URL of the page to clone.
        output_dir: Folder to write the clone into (created if missing).

    Returns:
        A dict with the generated index_path, css_dir, js_dir, and images_dir.
    """
    return clone_site(url, output_dir)


if __name__ == "__main__":
    mcp.run()
