class KeysAndRooms {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> roomsVisited = new HashSet<>();
        Stack<Integer> keys = new Stack<>();
        keys.push(0);
        while(!keys.empty()){
            int room = keys.pop();
            if(roomsVisited.contains(room))
                continue;
            for(Integer key : rooms.get(room)){
                keys.push(key);
            }
            roomsVisited.add(room);
        }
        return rooms.size() == roomsVisited.size();
    }
}