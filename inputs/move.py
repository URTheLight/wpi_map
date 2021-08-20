import sys
import math
import pandas as pd

country_dict = {'Afghanistan': 'AF', 'Åland Islands': 'AX', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ', 'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS', 'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 'Bolivia': 'BO', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Brazil': 'BR', 'British Indian Ocean Territory': 'IO', 'British Virgin Islands': 'VG', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Cape Verde': 'CV', 'Caribbean Netherlands': 'BQ', 'Cayman Islands': 'KY', 'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Christmas Island': 'CX', 'Cocos Islands': 'CC', 'Colombia': 'CO', 'Comoros': 'KM', 'Congo': 'CG', 'Cook Islands': 'CK', 'Costa Rica': 'CR', 'Croatia': 'HR', 'Cuba': 'CU', 'Curaçao': 'CW', 'Cyprus': 'CY', 'Czech Republic': 'CZ', 'Democratic Republic of the Congo': 'CD', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Dominican Republic': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Ethiopia': 'ET', 'Falkland Islands': 'FK', 'Faroe Islands': 'FO', 'Federated States of Micronesia': 'FM', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF', 'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT', 'Ivory Coast': 'CI', 'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', 'Kosovo': 'XK', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', 'Laos': 'LA', 'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macau': 'MO', 'Macedonia': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Marshall Islands': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Mayotte': 'YT', 'Mexico': 'MX', 'Moldova': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands': 'NL', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'North Korea': 'KP', 'Northern Mariana Islands': 'MP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Palestine': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines': 'PH', 'Pitcairn Islands': 'PN', 'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'Reunion': 'RE', 'Romania': 'RO', 'Russia': 'RU', 'Rwanda': 'RW', 'Saint Helena': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'São Tomé and Príncipe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Sint Maarten': 'SX', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Georgia and the South Sandwich Islands': 'GS', 'South Korea': 'KR', 'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR', 'Svalbard and Jan Mayen': 'SJ', 'Eswatini': 'SZ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syria': 'SY', 'Taiwan': 'TW', 'Tajikistan': 'TJ', 'Tanzania': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands': 'TC', 'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'United Arab Emirates': 'AE', 'United Kingdom': 'GB', 'United States': 'US', 'United States Minor Outlying Islands': 'UM', 'United States Virgin Islands': 'VI', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Vatican City': 'VA', 'Venezuela': 'VE', 'Vietnam': 'VN', 'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}

# read the data from the excel document
df = pd.read_excel("./wlg_country.xlsx")

# start from year 1870
curr_year = 1870
years = []
countries = []

# store country names in an array
for i in range (195):
    countries.append(df.at[i, "Country"])

'''
# 127 years in total
for span in range (127):
    select_year = curr_year + span
    year = df.loc[(df['Year'] == select_year), ["Country", "Country Code", "Z-Score"]]
    years.append(year)
    '''

# 195 countries every year
for i in range (127):
    select_year = curr_year + i
    #sys.stdout.write("var svgMapDataWPI" + str(select_year) + " = {\n  data: {\n    wpi: {\n      format: \'Z-Score: {0}\'\n    },\n    heatIndex: {\n      format: \'Visualized Index: {0} (for display only)\',\n      thresholdMax: 100,\n      thresholdMin: 0\n    }\n  },\n  applyData: \'heatIndex\',\n  values: {\n")
    sys.stdout.write("var svgMapDataWPI" + str(select_year) + " = {\n  data: {\n    heatIndex: {\n      thresholdMax: 100,\n      thresholdMin: 0\n    }\n  },\n  applyData: \'heatIndex\',\n  values: {\n")
    for j in range (195):
        row = i * 127 + j
        if df.at[row, "Country"] in country_dict:
            z = df.at[row, "Z-Score"]
            heat_index = 100 * (z - 0)
            sys.stdout.write("    " + country_dict[df.at[row, "Country"]] + ": { wpi: " + str(z) + ", heatIndex: " + str(heat_index) + "},\n")
    sys.stdout.write("  }\n}\n\n")