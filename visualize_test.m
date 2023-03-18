out_oura = importfile('./oura_csv_out.csv');

out_oura.Date.Format = 'dd.MM.uuuu HH:mm';
out_oura.Time.Format = 'dd.MM.uuuu HH:mm';
myDatetime = out_oura.Date + timeofday(out_oura.Time);

%%
t =out_oura{:,4};
t = movmean(t,20);
figure; 
plot(myDatetime,t,'LineWidth',1.5,'Color','k')
ylabel('Heart Rate')