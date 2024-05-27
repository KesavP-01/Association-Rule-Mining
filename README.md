
# Market Basket Analysis

## Description:
This process involves analyzing shopping data to find patterns and associations between products that are frequently bought together. The analysis starts by reading the shopping order data and the product information. It identifies how often individual products and pairs of products are bought together.

## Steps Involved:

**Calculating Frequency and Support**: Determine how often each product is purchased and calculate the percentage of total orders this represents (support).

**Filtering Frequent Products**: Only products that meet a minimum threshold for support are considered further.

**Identifying Product Pairs**: Find all unique pairs of products that are bought together in the same order and calculate their combined frequency and support.

**Calculating Confidence and Lift**: Evaluate the likelihood that buying one product will lead to buying another (confidence) and measure the strength of these associations (lift).

**Ranking Associations**: The product pairs are then sorted by their lift value to highlight the strongest associations.

Finally, the product names are added to these associations for easier interpretation, resulting in a list of product pairs with their support, confidence, and lift values, sorted by the strength of their association. This helps in understanding which products are commonly bought together, aiding in inventory management, marketing strategies, and improving customer experience.

## Results
![Assoc](https://github.com/KesavP-01/Association-Rule-Mining/assets/161378031/66308ef8-1681-40af-bdcf-810d5d4699b8)
#### The results show us the lift associated to each product pair. Higher the lift, higher the chance of customer buying those products together. 


For Example, a person who bought **Organic Strawberry Chia Lowfat 2% Cottage Cheese** is **10 times** more likely to buy **Organic Cottage Cheese Blueberry Acai Chia** than a person who did not buy **Organic Strawberry Chia Lowfat 2% Cottage Cheese**.