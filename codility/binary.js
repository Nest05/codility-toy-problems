function solution(N) {
    const binary = N.toString(2);
    let longestGap = 0;
    let currentGap = 0;
    let counting = false;

    for(let i=0; i < binary.length; i++){
        if(binary[i] === '1'){
            counting = true;

            if(currentGap > 0 && currentGap > longestGap){
                longestGap = currentGap;
            }
            currentGap = 0;
        }else if(counting){
            currentGap++;
        }
    }
    return longestGap;
}