clc

%Pearson£¨Spearmanœ‡πÿæÿ’Û£®100°¡100£©
pearson=zeros(100,100);
spearman=zeros(100,100);

database={x000001,x000006,x000012,x000014,x000016,x000021,x000025,x000026,x000027,x000028,
    x000036,x000039,x000043,x000046,x000049,x000055,x000059,x000060,x000062,x000063,
    x000065,x000069,x000078,x000088,x000089,x000090,x000096,x000402,x000404,x000410,
    x000417,x000418,x000419,x000420,x000421,x000422,x000423,x000425,x000428,x000501,
    x000507,x000510,x000514,x000521,x000523,x000525,x000528,x000530,x000531,x000532,
    x000538,x000539,x000541,x000543,x000544,x000548,x000550,x000551,x000554,x000559,
    x000563,x000565,x000567,x000568,x000570,x000572,x000573,x000576,x000581,x000589,
    x000591,x000597,x000598,x000599,x000601,x000609,x000610,x000619,x000623,x000627,
    x000632,x000635,x000637,x000659,x000661,x000667,x000680,x000685,x000690,x000692,
    x000698,x000700,x000701,x000702,x000703,x000705,x000707,x000708,x000713,x000717};

for i=1:100
    for j=1:100
       [pearson(i,j),spearman(i,j)]=first_4(database{i},database{j});
    end
end

csvwrite('pearson.csv',pearson);
csvwrite('spearman.csv',spearman);
ptemp=pearson;
stemp=spearman;
ptemp=ptemp(:)';
stemp=stemp(:)';
ptemp=abs(ptemp);
stemp=abs(stemp);
psort=sort(ptemp);
ssort=sort(stemp);
csvwrite('pearson_sort.csv',psort');
csvwrite('spearman_sort.csv',ssort');
%5pair 
for i=1:5
    pnegetive(i)=find(ptemp==psort(2*i-1),1,'first');
    ppositive(i)=find(ptemp==psort(10000-100-2*i+1),1,'first');
    snegetive(i)=find(stemp==ssort(2*i-1),1,'first');
    spositive(i)=find(stemp==ssort(10000-100-2*i+1),1,'first');
end

% %positon 
for i=1:5
    ppos(2*i-1)=fix(ppositive(i)/100)+1;
    spos(2*i-1)=fix(spositive(i)/100)+1;
    pneg(2*i-1)=fix(pnegetive(i)/100)+1;
    sneg(2*i-1)=fix(snegetive(i)/100)+1;
    
    spos(2*i)=mod(spositive(i),100);
    ppos(2*i)=mod(ppositive(i),100);
    pneg(2*i)=mod(pnegetive(i),100);
    sneg(2*i)=mod(snegetive(i),100);
end

for i=1:10
    ppdata{i}=database{ppos(i)};
    pndata{i}=database{pneg(i)};
    spdata{i}=database{spos(i)};
    sndata{i}=database{sneg(i)};
end

for i=1:5
       [pr1(i),pr2(i),ppp(i),pps(i)]=first_6(ppdata{2*i-1},ppdata{2*i});
       [nr1(i),nr2(i),pnp(i),pns(i)]=first_6(pndata{2*i-1},pndata{2*i});
       [pr1(i),pr2(i),spp(i),sps(i)]=first_6(spdata{2*i-1},spdata{2*i});
       [nr1(i),nr2(i),snp(i),sns(i)]=first_6(sndata{2*i-1},sndata{2*i});
end

ppp
pps
pnp
pns
spp
sps
snp
sns

