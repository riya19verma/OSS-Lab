#include <stdio.h>

int main() {
    int n, i;
    int numbers[100]; // You can adjust this size as needed
    int sum = 0;
    float average;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    if (n <= 0 || n > 100) {
        printf("Invalid number of elements. Must be between 1 and 100.\n");
        return 1;
    }

    printf("Enter %d integers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &numbers[i]);
        sum += numbers[i];
    }

    average = (float)sum / n;
    printf("The average is: %.2f\n", average);

    return 0;
}
