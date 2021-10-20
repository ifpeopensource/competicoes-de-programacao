#include <cstdio>

int main() {
    int distance;
    scanf("%d", &distance);

    printf("%d\n", (distance - 5) % 8);
}