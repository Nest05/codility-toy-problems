function solution(A, K) {
    const N = A.length;

    if (N === 0 || K === 0) {
        return A;
    }

    K = K % N;

    if (K === 0){
        return A;
    }

    const suffix = A.slice(N - K);
    const prefix = A.slice(0, N - K);
    const rotatedArray = suffix.concat(prefix);

    return rotatedArray;
}