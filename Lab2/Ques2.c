#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 500
#define WORD_LENGTH 30

int main() {
    char paragraph[1000];
    char words[MAX_WORDS][WORD_LENGTH];
    int wordCount[MAX_WORDS] = {0};
    int totalWords = 0;
    printf("Enter a paragraph:\n");
    fgets(paragraph, sizeof(paragraph), stdin);
    for (int i = 0; paragraph[i] != '\0'; i++) {
        if (ispunct(paragraph[i])) {
            paragraph[i] = ' ';
        }
        paragraph[i] = tolower(paragraph[i]);
    }
    char *currentWord = strtok(paragraph, " \n\t");

    while (currentWord != NULL) {
        int found = 0;
        for (int i = 0; i < totalWords; i++) {
            if (strcmp(words[i], currentWord) == 0) {
                wordCount[i]++;
                found = 1;
                break;
            }
        }

        if (!found) {
            strcpy(words[totalWords], currentWord);
            wordCount[totalWords] = 1;
            totalWords++;
        }

        currentWord = strtok(NULL, " \n\t");
    }
    printf("\nWord Frequencies:\n");
    for (int i = 0; i < totalWords; i++) {
        printf("%s: %d\n", words[i], wordCount[i]);
    }

    return 0;
}
