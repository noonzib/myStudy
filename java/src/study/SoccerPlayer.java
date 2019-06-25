package study;

public class SoccerPlayer {
    int str = 100; //공격력
    int def = 70; // 수비력

    //공격중심
    public void offensive(){
        str += 10;
        def -= 10;
    }

    // 수비중심
    public void defensive(){
        str -= 10;
        def += 10;
    }
}
