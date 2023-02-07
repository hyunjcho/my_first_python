#!/tool/pandora/bin/perl
#use strict;
#
#Downloads
$file = "C:\\Users\\jinc.SILVACOCORP.000\\Downloads\\quotes.csv";

$trend_file = "C:/Users/jinc.SILVACOCORP.000/OneDrive/Script/money.csv";
$out_file = "C:/Users/jinc.SILVACOCORP.000/OneDrive/Script/new_money.csv";


open(AXT, ">$out_file") or die "Can't write to $out_file: $! \n";

open(FILE, $trend_file) || die "I can't open $trend_file!\n";
chomp(@trend_data = <FILE>);
close FILE;

@trend_symbol = split(/,/,$trend_data[0]);

# current_gain
$previous = $trend_data[$#trend_data];
# Money invested in stock
#$current_cost = (split/,/,$trend_data[0])[0];
# accumurated profit
$accumurated_profit = (split/,/,$trend_data[1])[0];
# cash balance
$cash_total = (split/,/,$trend_data[2])[0];

# total gain yesterday
$day_before_gain = (split/,/,$previous)[$#trend_symbol-10];
# total invest yesterday
$day_before_cost = (split/,/,$previous)[$#trend_symbol-2];
# total accu_prof yesterday
$day_before_accu = (split/,/,$previous)[$#trend_symbol-0];


#printf ("$day_before_gain\n");
#printf ("$day_before_cost\n");

shift(@trend_symbol);
@trend_transposed = transpose_csv(@trend_data);

open(FILE, $file) || die "I can't open $file!\n";
chomp(@input_data = <FILE>);
close FILE;
$cdx = "option,1,,,,,,,,,,,,,";
push(@input_data,$cdx);
$cdx = "CD,100,,,,,,,,,,,,,";
push(@input_data,$cdx);

shift(@input_data);
    $day = (split/,/,$input_data[0])[2];
    $hour = (split/,/,$input_data[0])[3];
    $hour =~ s/ EST//g;
    $date = $day."_".$hour;
    

# This is for writing previous data
foreach (@trend_data) { printf AXT ("$_\n");}

# New data start from the date
printf AXT ("$date,");

$sum=$market_value=$money_invested=0;
foreach $gg (@trend_symbol) {
    @aa=@bb=();
    @aa = grep {/^$gg,/} @input_data;
    $price = (split/,/,$aa[0])[1];
    @bb = grep {/^$gg,/} @trend_transposed;
    $share_number = (split/,/,$bb[0])[1];
    $share_paid = (split/,/,$bb[0])[2];

    $xgain = ($price - $share_paid)*$share_number;
    $xcost = $share_paid * $share_number;
    $sum = $sum + $xgain;
    $money_invested = $money_invested + $xcost;
    #printf ("$gg,$xgain,$sum\n");

# output is to write the output of the entry default is current stock price
    $output = $price;

    $mark = $price * $share_number;
    # total current market value
    $market_value = $market_value + $mark;
printf ("$market_value\n");

    # current stock gain
    $current_stock_gain = $market_value - $money_invested;

    #printf ("market value: $market_value\n");
    ##	printf ("money invested: $money_invested\n");
    #printf ("stock gain: $current_stock_gain\n");

    # yesterday stock gain
    # $day_before_gain
    # Daily Gain
    $daily_accu = $accumurated_profit -$day_before_accu;

    #printf ("day_before_gain: $day_before_gain\n");
    #printf ("daily_accu: $daily_accu\n");

    #$daily_gain = $current_stock_gain - $day_before_gain+$daily_accu;
    #printf ("daily_gain: $daily_gain\n");
    

    # fidelity = current market value + current cash
    $fidelity_total = $market_value + $cash_total;

    # total profit 
    $total_profit = $current_stock_gain + $accumurated_profit;

    # for 2019
    $Ygain = $total_profit-109400.53;
    # for 2020
    $Ygain = $total_profit-205929.30;
    $yearly_gain = $total_profit/211379.05 - 1;
    $daily_gain = $Ygain - $day_before_gain;
    #printf ("daily_gain: $Ygain,$day_before_gain,$daily_gain\n");

    if ($gg eq "SPY") {
    	$output = $price*10 if $gg eq "SPY"; 
    	$Ysnp = 100*($price*10/3248.7-1);
	#printf("$price,$Ysnp\n");
    }
    $output = $Ysnp if $gg eq "Ysnp";
    $output = $Ygain if $gg eq "Ygain"; 
    $output = $yearly_gain*100 if $gg eq "Yearly"; 
    $output = $current_stock_gain if $gg eq "Current_gain"; 
    $output = $total_profit if $gg eq "Profit";
    $output = $daily_gain if $gg eq "Daily_Gain";
    $output = $market_value if $gg eq "MarketValue";
    $output = $fidelity_total if $gg eq "Fidelity";
    $output = $cash_total if $gg eq "Cash_Balance";
    $output = $money_invested if $gg eq "Money_invest";
    $output = $market_value/$fidelity_total*100 if $gg eq "ratio";
    $output = $accumurated_profit if $gg eq "accu_prof";

    #printf ("$gg, $output, $sum \n");
    printf AXT ("%.2f,",$output);
}
    printf AXT ("\n");

printf ("Updating Yahoo table at $date \n");

system "del $file";


sub transpose_csv {
	@onx=@tmp=@tran=@data=();
	my @onx = @_;
my @tmp = split (/,/, $onx[0]);

$num_row = $#onx+1;
$num_col = $#tmp+1;

#printf ("$num_row, $num_col\n");

for($i=0;$i<$num_row;$i++){
	@line=();
	@line = split(/,/,$onx[$i]);
for($j=0;$j<$num_col;$j++){
	$data[$i][$j]=$line[$j];
}
}

for($j=0;$j<$num_col;$j++){
	$new_line = "";
for($i=0;$i<$num_row;$i++){
	$new_line = $new_line.",".$data[$i][$j];
}
  $new_line =~ s/^,//;
  push(@tran, $new_line);
#printf ("$new_line\n");
	
}
return @tran;
}
