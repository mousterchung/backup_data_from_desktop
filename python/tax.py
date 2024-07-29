def postTaxPrice(price):
    ans=price*1.08
    return ans

print(tax.postTaxPrice(100),"元")
print(tax.postTaxPrice(128),"元")
print(tax.postTaxPrice(980),"元")
