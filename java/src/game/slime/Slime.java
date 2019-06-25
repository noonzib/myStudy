package game.slime;

public class Slime {
    String name;
    int hp;

    public Slime(String n){
        name = n;
    }
    public void attack(){
        System.out.println(name+"는 인간을 공격했습니다");
    }
}
