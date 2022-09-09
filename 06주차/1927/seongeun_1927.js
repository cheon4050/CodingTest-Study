/*
* 널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
*
* <입력>

* 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
* 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
* 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
* x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
* x는 2^31보다 작은 자연수 또는 0이고, 음의 정수는 입력으로 주어지지 않는다.
* */

// const [n, ...arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = 9;
const input=[0,12345678,1,2,0,0,0,0,32];
// let fs = require('fs');
// var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// // let input = fs.readFileSync(__dirname + '/stdin.txt').toString().replace(/\r/g, "").trim().split('\n');
// let n = +input[0]
let operations = []
for (let i = 1; i < input.length; i++) {
    operations.push(input[i])
}

class MinHeap {
    constructor() {
        this.nodes = []
    }

    insert(data) {
        this.nodes.push(data)
        this.bubbleUp()
    }

    bubbleUp(index = this.nodes.length - 1) {
        if (index < 1) return
        const currentNode = this.nodes[index]
        const parentIndex = Math.floor((index - 1) / 2)
        const parentNode = this.nodes[parentIndex]
        // 부모값이 더 작으면 끝내기
        if (parentNode <= currentNode) return
        // 그렇지 않으면 자리바꾸기
        this.nodes[index] = parentNode
        this.nodes[parentIndex] = currentNode
        index = parentIndex
        this.bubbleUp(index)
    }

    extract() {
        const min = this.nodes[0]
        if (this.nodes.length === 1) {
            this.nodes.pop()
            return min
        }
        this.nodes[0] = this.nodes.pop()
        this.trickleDown()
        return min
    }

    trickleDown(index = 0) {
        const leftChildIndex = index * 2 + 1
        const rightChildIndex = index * 2 + 2
        const length = this.nodes.length
        let minimum = index
        if (!this.nodes[leftChildIndex] && !this.nodes[rightChildIndex]) return;
        if (!this.nodes[rightChildIndex]) {
            if (this.nodes[leftChildIndex] < this.nodes[minimum]) {
                minimum = leftChildIndex
            }
        }
        if (this.nodes[leftChildIndex] > this.nodes[rightChildIndex]) {
            if (rightChildIndex <= length && this.nodes[rightChildIndex] < this.nodes[minimum]) {
                minimum = rightChildIndex
            }
        } else {
            if (leftChildIndex <= length && this.nodes[leftChildIndex] < this.nodes[minimum]) {
                minimum = leftChildIndex
            }
        }
        if (minimum !== index) {
            let t = this.nodes[minimum]
            this.nodes[minimum] = this.nodes[index]
            this.nodes[index] = t
            this.trickleDown(minimum)
        }
    }
}
const heap = new MinHeap()
let extracts = ''
operations.forEach((e, index) => {
    if (e !== 0) {
        heap.insert(e)
    } else {
        if (heap.nodes.length === 0) {
            extracts += '0' + '\n'
        } else {
            let t = heap.extract()
            extracts += t + '\n'
        }
    }
})

console.log(extracts.trim())

/*
* 비어있지 않으면 : 일단 push하고, push된 가장 마지막 원소를 부모노드와 비교해간다.
부모노드의 index: (현재 노드의 index - 1) / 2
부모노드보다 값이 크면? 문제 ㄴㄴ
값이 작으면? 부모-자식 관계가 바뀌어야 하므로, 서로 swap한다.
*
* 현재 힙이 비어있으면 : 그냥 0만 출력한다.
*
* 비어있지 않으면 :
힙의 길이가 1이면 : pop하고 해당 원소를 return한다.
1보다 더 크면 : 루트 노드를 먼저 꺼내고, 현재 힙에 있는 가장 마지막 노드를 루트 자리에 놓는다.
그리고 부모-자식 관계를 재정리한다.
왼쪽 자식 index: (현재 노드의 index × 2) + 1
오른쪽 자식 index: (현재 노드의 index × 2) + 2
*
* */