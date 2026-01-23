#include <stdio.h>
#include <stdbool.h>

int main() {
    // TEMPERATURE CONVERTER
    int choice = 0;
    bool loop = true;
    float celsius = 0.0f;
    float fahrenheit = 0.0f;
    
    printf("Temperature Conversion Calculator\n");

    while (loop == true) {
        printf("1. Celsius to Fahrenheit\n");
        printf("2. Fahrenheit to Celsius\n");
        printf("Enter choice (1 or 2): ");
        scanf("%d", &choice);
        
        if (choice == 1) {
            // Celsius to Fahrenheit
            printf("Enter temperature in Celsius: ");
            scanf("%f", &celsius);
            fahrenheit = (celsius * 9.0 / 5.0) + 32;
            printf("In Fahrenheit: %.3f\n", fahrenheit);
            loop = false;
        }
        else if (choice == 2) {
            // Fahrenheit to Celsius
            printf("Enter temperature in Fahrenheit: ");
            scanf("%f", &fahrenheit);
            celsius = (fahrenheit - 32) * 5.0 / 9.0;
            printf("In Celsius: %.3f\n", celsius);
            loop = false;
        }
        else {
            printf("Invalid choice! Please enter 1 or 2\n\n");
        }
    }
    
    return 0;
}
