custom code for Biographien

needs to be included into the an apis project via symlink
on windows e.g.
`C:\Users\pandorfer\Documents\Redmine\apis\biographien>mklink /d theme "C:\Users\pandorfer\Documents\Redmine\apis\themes\`

you also have to ovveride your custom-apis-settings-file e.g. `{myapisprocet}/apis/settings/server.py` by adding this line:
`INSTALLED_APPS = INSTALLED_APPS + ['theme']`


for the FEATURED COLLECTION feature, add the constant to your custom settings-file:
`FEATURED_COLLECTION_NAME = "FEATURED"`
and add a Person to this collection


Provide a string matching the `text.kind` you'd like to display as 'main_text' in your custom settings-file:
`MAIN_TEXT_NAME = "ÖBL Haupttext"`
