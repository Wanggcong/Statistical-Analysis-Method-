function[data,price]=getDatePrice(csv_data)
date = csv_data(:,1);
high_price = csv_data(:,4);
low_price = csv_data(:,5);
price = ((high_price + low_price)/2);
