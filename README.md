# Truck Scheduling for Woolworths NZ
Woolworths NZ operates the Woolworths, FreshChoice and SuperValue supermarket chains in New Zealand. Each store needs to receive goods daily to ensure their shelves are fully stocked. They operate a fleet of 24 trucks in order to move these goods from their distribution centre in Favona to their stores around Auckland.

On each day, each store receives pallets of goods from a distribution centre based on store sales. Therefore, the number of pallets shipped to each store differs each day. For this model, we will work in units of pallets, and we will not differentiate between different product categories.

Each truck can carry up to 20 pallets of goods, and operates on a trip schedule that will have each truck deliver goods to a selection of stores, and return to the warehouse. Once at the store, a pallet takes on average 10 minutes to unload. 

Current policy requires each scheduled trip take no more than four hours, on average, to complete; this includes both driving time and unloading time. Each truck costs $250 per hour to operate and can operate two (approximately) four-hour shifts per day. You may assume that the two shifts start at 8am or 2pm, and that each store only receives one delivery per day.

However, traffic conditions on Auckland roads are not always ideal, so the driving time required may well be longer or shorter depending on the time of day. This means some trucks may take more than four hours to complete their trip. In such cases, the extra time costs Woolworths NZ $325 per hour.

On days where there are not sufficient trucks to satisfy all demand, either because of a shortage of truck time or an excess in store demand for pallets, additional trucks can be ‘wet-leased’ (vehicle rental that includes a driver) from Mainfreight for a cost of $2300 for every four hours of on-duty time, charged in four-hour blocks.


# Woolworths NZ would like to determine a suitable truck logistics plan such that costs are minimised. They have provided you with:

the number of pallets delivered to each store they operate over a 4 week period: WoolworthsDemand2024.csvDownload WoolworthsDemand2024.csv

the GPS coordinates of each store: WoolworthsLocations.csvDownload WoolworthsLocations.csv

the travel durations (in seconds) between each pair of stores and distribution points: WoolworthsDurations.csvDownload WoolworthsDurations.csv

Map of all locations to assist you: Woolworths2024Map.png

Given the cost of operations, Woolworths NZ would like to outsource more of their logistics to Mainfreight by reducing their own logistics fleet and allowing Mainfreight to do more deliveries. Each Woolworths truck incurs approximately $75,000 in maintenance and other costs per year.


# Part I
Analyse the data provided to develop an appropriate estimate of the number of pallets required at each store on each day.
  
Using the pallet estimates, create a set of feasible trucking routes that satisfy the requirements given.
  
Formulate and solve a mixed-integer program to find the least-cost routing schedule for the truck fleet, using the demand estimates from part 1. This should also sensibly address the outsourcing proposal.


# Part II
Create visualisation(s) of your proposed trucking routes, suitable for presentation to management.
  
Evaluate the quality of your schedule by creating a simulation to estimate the actual cost of satisfying all pallet demand at every store. Your simulation should take into variations in demand and sensibly approximate the effect of traffic. Simulation can also assist you in analysing the outsourcing proposal.
  
Discuss the impact of Woolworths’ outsourcing proposal in terms of wider implications on the systems and people that interact with this truck logistics plan.
  
What are your recommendations to Woolworths NZ after conducting this study?
