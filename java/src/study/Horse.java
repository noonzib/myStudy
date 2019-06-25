package study;

public class Horse {
    String name;

    Horse(String n){
        name = n;
    }
    void run(){

    }
}
class Unicorn extends Horse {
    int fp;

    Unicorn(String n){
        super(n);
    }
    void fly(){

    }
}

