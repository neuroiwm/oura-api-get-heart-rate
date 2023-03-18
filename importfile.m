function ouracsvout = importfile(filename, dataLines)
%% Input handling

% If dataLines is not specified, define defaults
if nargin < 2
    dataLines = [2, Inf];
end

%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 5);

% Specify range and delimiter
opts.DataLines = dataLines;
opts.Delimiter = ["+", ",", "T"];

% Specify column names and types
opts.VariableNames = ["Date", "Time", "Null", "BPM", "State"];
opts.VariableTypes = ["datetime", "datetime", "categorical", "double", "categorical"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";
opts.ConsecutiveDelimitersRule = "join";

% Specify variable properties
%opts = setvaropts(opts, ["BPM", "VarName5"], "EmptyFieldRule", "auto");
opts = setvaropts(opts, "Date", "InputFormat", "yyyy-MM-dd");
opts = setvaropts(opts, "Time", "InputFormat", "HH:mm:ss");
%opts = setvaropts(opts, "State", "ThousandsSeparator", ",");

% Import the data
ouracsvout = readtable(filename, opts);

end