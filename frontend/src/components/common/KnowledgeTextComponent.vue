<template>
  <template
    v-for="(s, i) in parse(text)"
    :key="i"
  >
    <br
      v-if="/\r?\n/g.test(s)"
    />
    <a
      v-else-if="/(https?:\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/i.test(s)"
      :href="s"
      target="_blank"
    >
      {{ s }}
    </a>
    <span
      v-else
    >
      {{ s }}
    </span>
  </template>
</template>

<script lang="ts" setup>
const parse = (text: string): string[] => {
    const result: string[] = [];
    text.split(/\r?\n/g).forEach((t: string) => {
        if (t) {
            result.push(...hyperlink([ t ]));
            result.push('\n');
        }
    });
    result.pop();
    return result;
};

const hyperlink = (source: string[]): string[] => {
    const s = source.pop();
    if (!s) {
        return [];
    }
    const m = s.match(/^(.*?)(https?:\/\/[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+&@#/%=~_|])(.*)/i);
    if (!m) {
        return source.concat(s);
    }
    let count = 0;
    [...Array(m.length - 1)].forEach((_, i) => {
        if (m[i + 1]) {
            source.push(m[i + 1]);
            count++;
        }
    });
    return (count > 1) ? hyperlink(source) : source;
};

defineProps<{
    text: string,
}>();
</script>
