class UndergroundSystem {
    Map<Integer, Pair<String, Integer>> checkInMap = new HashMap<>();
    Map<String, Pair<Double, Integer>> routeMap = new HashMap<>();
    
    
    public UndergroundSystem() {
        
    }
    
    public void checkIn(int id, String stationName, int t) {
        checkInMap.put(id, new Pair<>(stationName, t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        Pair<String, Integer> checkInInfo = checkInMap.get(id);
        checkInMap.remove(id);
        
        String routeName = checkInInfo.getKey() + "_" + stationName;
        Integer checkInTime = checkInInfo.getValue();
        
        Pair<Double, Integer> oldRoute = routeMap.getOrDefault(routeName, new Pair<>(0.0, 0));
        routeMap.put(routeName, new Pair<> ( (oldRoute.getKey()*oldRoute.getValue()+(t-checkInTime))/(oldRoute.getValue()+1), oldRoute.getValue()+1) );
        
        
    }
    
    public double getAverageTime(String startStation, String endStation) {
        return routeMap.get(new String (startStation + "_" + endStation) ).getKey();
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */