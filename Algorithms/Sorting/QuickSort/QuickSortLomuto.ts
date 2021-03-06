export function quickSortLomuto(array: number[]): void {
  quickSortRecursive(array, 0, array.length - 1);
}

function quickSortRecursive(array: number[], low: number, high: number): void {
  if (low < high) {
    const pivot = randomPartition(array, low, high);
    quickSortRecursive(array, low, pivot - 1);
    quickSortRecursive(array, pivot + 1, high);
  }
}

function randomPartition(array: number[], low: number, high: number): number {
  const random = Math.floor(Math.random() * (high - low)) + low;
  [array[random], array[high]] = [array[high], array[random]];
  return partition(array, low, high);
}

function partition(array: number[], low: number, high: number): number {
  let i = low;

  for (let j = low; j < high; j++) {
    if (array[j] <= array[high]) {
      [array[j], array[i]] = [array[i], array[j]];
      i++;
    }
  }

  [array[i], array[high]] = [array[high], array[i]];
  return i;
}
