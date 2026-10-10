# Turtle Cleaning Services — quote request form

Live: https://cruedadiaz2-cpu.github.io/turtle-quote-calculator/
Link-in-bio page (for Instagram / Facebook): `/links/`

## How it works

The page itself has no server. Since Oct 10, 2026 the main button, **Send my request**,
and the **Call me back** box at the top POST the request to a Google Apps Script web app
owned by `managturtlecs@gmail.com` ("Turtle - Quote Form Receiver"). It appends one row
to the "Turtle — Quote Requests" sheet (Channel "Web form (<source>)", Source ID
`web:<id>`) and emails an alert whose subject starts "Turtle lead", so the daily
`turtle-sync-cotizaciones` task does not copy it a second time. The receiver's code
lives in the vault: `💼 Business/Turtle Cleaning Services LLC/Apps Script - Quote Form Receiver.gs`.

If the POST fails, the page opens the older routes, which hand the summary to another
app where the visitor still has to press send:

- **Send by WhatsApp** → `wa.me` link to (908) 880-5716
- **Send by email** → the device's mail app (`mailto:`)
- **Open Gmail instead** → Gmail web compose, for devices with no mail app

Why the change: from the Facebook and Instagram in-app browser almost nobody finished
those hand-offs (11 ad visits on Oct 8-9, 0 requests).

A banner with the 5% first-cleaning offer shows until the end of Oct 15, 2026 (New York)
and hides itself after that.

Every request names where the visitor came from. The form adds a `Source:` line and the
WhatsApp buttons on `/links/` and `/chat/` add `(via Instagram)`, `(via Facebook)` or
`(via Google)` to the greeting. The source comes from `?src=` (only `instagram`, `ig`,
`facebook`, `fb`, `google`), then the Instagram or Facebook in-app browser, then the
referrer. With no known source nothing is added.

No prices live in this page. Quotes are sent by reply — deliberately, so nothing
in the page source reveals the rate card.

## Editing it

Edit `src/page.html`, then:

    python src/build.py

That inlines the logos and writes `index.html`. Commit and push — GitHub Pages
redeploys in a couple of minutes.

Do **not** edit `index.html` directly; it is generated and your change would be
overwritten on the next build.

## Moving it to turtlecleaningusa.com

`index.html` is fully self-contained (logos included as data URIs), so it can be
uploaded on its own to any host. For a subdomain on GitHub Pages instead, add a
CNAME record pointing `cotiza` → `cruedadiaz2-cpu.github.io` at the DNS provider
(Hostinger), then set the custom domain in the repo's Pages settings — in that
order, or the live site goes down while DNS catches up.
