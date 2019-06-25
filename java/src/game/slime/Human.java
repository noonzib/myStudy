package game.slime;

public class Human {
    String name;
    int hp = 100;

    public Human(String n){
        name = n;
    }

    public void attack(String sName) {
        System.out.println("인간은 "+sName+"를 공격했습니다");
    }
}
