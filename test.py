import pandas as pd

values = [
    ['Country', 'ISO Code', 'Region', 'ADM1', 'Affected Pop Share', 'Type', 'Meta (e.g. group size thresholds', 'Start', 'End', 'Source', 'Comment'],
    ['English', 'ISO 3166-2', '', 'Nationwide=Empty\nRegional=Use ADM1-codes (sheet)', 'Esimate of affected population, if a measure is below ADM1 level (e.g. city).', 'Refer to instructions sheet', 'Meta information', 'First day the measure was active', 'Last day the measure was active', 'Link'],
    ['Belgium', 'BE', '', '', '1,00', 'Border Closing', '', '20.3.2020', '', 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Belgium'],
]

column_names = values.pop(0)
df = pd.DataFrame(
    [row + ['']*(len(column_names) - len(row)) for row in values],
    columns=column_names
)

print(df)
