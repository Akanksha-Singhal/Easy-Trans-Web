import java.time.LocalTime;  
import java.util.ArrayList;
class Stop
{
    double longitude;
    double latitude;
    int StopCode;
    String StopName;
    int duration; 

    Stop(double longitude, double latitude,  String StopName, int StopCode, int duration)
    {
        this.latitude  = latitude;
        this.longitude = longitude;
        this.StopName  = StopName; 
        this.StopCode  = StopCode;   
        this.duration  = duration;     
    }
}

class Route
{
    String RouteNo;
    ArrayList<Bus> buses = new ArrayList<Bus>();
    Stop stops[];

    
    Route(String RouteNo, Stop stops[])
    {
        this.RouteNo = RouteNo;
        this.stops = stops;
    }

    void assignBustoRoute(Bus bus)
    {
        this.buses.add(bus);
        bus.assignRoute(this);   
    }

    void startBus(Bus bus)
    {
        bus.startTime = LocalTime.now();
        bus.runningStatus = true;
        System.out.println("Bus "+bus.busNo+" starts on Route No: "+ this.RouteNo+ " at time: "+ bus.startTime);
        bus.start();
    }

}

class Ticket
{ 

    int noOfMales; // toal
    int noOfFemales; // 75%; ciel
    int noOfStudent; //0.5 ciel
    int noOfChildren; // 0.5%
    int start_stop;
    int end_stop; 
    float price ;    // 0.90 Rs/km

    public void createTicket(int noOfMales, int noOfFemales, int noOfStudent, int noOfChildren, int end_stop)
    {
        this.noOfMales = noOfMales;
        this.noOfFemales = noOfFemales;
        this.noOfStudent = noOfStudent;
        this.noOfChildren = noOfChildren;
    }
}

class Bus extends Thread
{
    int curr_latitude;
    int curr_longitude;
    int busNo;
    Route route;
    int startStop;
    int endStop;
    int totalNoOfPassengers;
    int curr_stop;
    int next_stop;
    LocalTime startTime = LocalTime.now(); 
    boolean runningStatus = false;    

    Bus(int busNo)
    {
       this.busNo = busNo;
    }

    void assignRoute(Route r)
    {
        this.route = r;
    }

    void getNextStop() 
    {   
        try
            {   System.out.println(this.route.stops[0].duration*1000);
                Thread.sleep(this.route.stops[0].duration*1000);
                System.out.println("This ")
            }
        catch(InterruptedException e)
        {

        }
        System.out.println("First stop : "+ this.route.stops[0].StopName);
    }

    public void run()
    {
        System.out.println("Bus started..");
        getNextStop();
    }
}

class Test
{
    public static void main(String args[])
    {
        Bus t1 = new Bus(1);

        //starting the thread
        Stop[] stops = new Stop[]{new Stop(27.028486, 75.769043, "Todi",       1000, 10), 
                                  new Stop(26.9181  , 75.8498,   "Galta Gate", 1001, 20)
                                 };

        Route r1 = new Route("R1", stops);
        r1.assignBustoRoute(t1);
        r1.startBus(t1);
   }   
}
    