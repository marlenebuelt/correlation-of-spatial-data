# correlation-of-spatial-data

## DropMunics
Determines which municipalities we drop according to the dropfile csv.

## DropMunics_2
Drops all munics with more than 4 missing values in row.

## FillMissingValues
fills missing valuesand returns five csv files

## MissingByDateAndMunic
returns a large table of missing observations by date and municipalities

## MissingCumulativesPerLocation
Cumulative sums of missing weeks

## MissingObsByDate
returns how many municipalities didn't enter values on a specific date. Returns five seperate files due to merge errors.

## MissingObsBySubperiod
Number, percent and max length of missing obs

## SpatialCorrelation
plots all locations and the weeks missing in summer 2015

## MissingMunicsPlot
attempts to plot the timeline per municipality showing missing and non-missing in different colors (not done yet)

## SubperiodsBeforeDrop
slices the original file into subperiods

## SubperiodsDates
all dates of the subperiods are saved here.

## SubperiodsPaths
provides get() and set() methods for all files. Change paths to your local folders here.
