function solution(operations) {
    const queue = new DoublePriorityQueue();

    operations.forEach(operation => {
        const [command, number] = operation.split(' ');
        if (command === 'I') queue.insert(+number);
        if (command === 'D') queue.delete(number);
    });

    return queue.isEmpty() ? [0, 0] : [queue.max, queue.min];
}

class DoublePriorityQueue {
    queue = [];

    insert(number) {
        this.queue.push(number);
        this.queue.sort((a, b) => a - b);
    }

    delete(type) {
        if (type === 1) this.queue.pop();
        if (type === -1) this.queue.shift();
    }

    isEmpty() {
        return this.queue.length === 0;
    }

    get max() {
        return this.queue[this.queue.length - 1];
    }

    get min() {
        return this.queue[0];
    }
}

console.log(solution(['I 16', 'I -5643','D -1','D 1','D 1','I 123','D -1']));
console.log(solution(['I -45', 'I 653', 'D 1', 'I -642','I 45','I 97','D 1','D -1','I 333']));


/**
  삭제를 할 때 최대값, 최소값을 구한 뒤 삭제 해주는 방법으로 진행
 먼저 I가 첫번째 알파벳일 경우는 그냥 queue에 넣어줬고
 D 1 일때는 최대값을 splice를 이용하여 빼주고
 D -1 일때는 최소값을 splice를 이용해서 빼줬다.
 그리고 마지막에 queue의 길이가 0이라면 [0,0]을 리턴해주고 그렇지 않다면
 정렬 후 최대 값 최소 값 을 리턴
 * **/