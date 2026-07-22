#include <stdio.h>

int main() {
    // This is main function.
    print_speed(30);
}

int print_speed(obj_speed) {
    float object_speed = obj_speed;

    if(object_speed <= 30) {
        printf("[OK] Object speed is %f", object_speed);
    } else {
        printf("[ERROR] Object speed is %f", object_speed);
    }
    return 0;
}