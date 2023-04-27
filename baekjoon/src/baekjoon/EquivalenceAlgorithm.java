package baekjoon;

public class EquivalenceAlgorithm {

    public static void equivalence(int m, int n, int[][] pairs) {
        int[] SEQ = new int[n + 1];
        int[] BIT = new int[n + 1];

        int[] DATA = new int[2 * m + 1];
        int[] LINK = new int[2 * m + 1];

        // Initialize SEQ and BIT arrays to 0
        for (int i = 1; i <= n; i++) {
            SEQ[i] = BIT[i] = 0;
        }

        int av = 1;

        // Phase 1: Process all input
        for (int k = 0; k < m; k++) {
            int i = pairs[k][0];
            int j = pairs[k][1];

            DATA[av] = j;
            LINK[av] = SEQ[i];
            SEQ[i] = av;
            av++;

            DATA[av] = i;
            LINK[av] = SEQ[j];
            SEQ[j] = av;
            av++;
        }

        int index = 1;

        // Phase 2: Output all classes
        while (index <= n) {
            if (BIT[index] == 0) {
                System.out.print("A new class: " + index + " {");

                BIT[index] = 1;
                int ptr = SEQ[index];
                int top = 0;

                // Initialize stack
                int[] stack = new int[n];
                for (int i = 0; i < n; i++) {
                    stack[i] = 0;
                }

                // Find the entire class
                while (ptr != 0) {
                    int j = DATA[ptr];

                    if (BIT[j] == 0) {
                        System.out.print(j + " ");
                        BIT[j] = 1;

                        LINK[ptr] = top;
                        top = ptr;

                        ptr = SEQ[j];
                    } else {
                        ptr = LINK[ptr];
                    }
                }

                System.out.print("}\n");

                // Empty stack
                while (top != 0) {
                    ptr = DATA[top];
                    top = LINK[top];
                }
            }

            index++;
        }
    }

    public static void main(String[] args) {
        int[][] pairs = {
            {2, 4}, {1, 3}, {2, 8}, {6, 5}, {7, 9}, {10, 6}, {3, 7}
        };

        equivalence(7, 10, pairs);
    }
}

