# Proposal 03.1 - Shader IO generation and package reading changes

[Criticality-Level: Level 2](https://troblecodings.github.io/data-diagrams/criticality-level.html)

## Current situation

Currently all shaders have to be written manuel. They are not being included within the packaging of the game nor are there pipe being generated automatically. All surrounding resources such as per index buffer and push const memory are hard coded and not dynamic.

## Problem

Pipeline creation, shader usage as well as buffers used in the draw are not being automatically build from what the artist supplies. As well as they are not included in the game package, rather they are compiled down into C code.

## Solution

The solution would be to introduce two new sections in the package loading system. The first one would include shaders, the second would include the pipe information. This would enable us to dynamically create pipelines and shaders for each material. Furthermore this should be tied to the material which then contains the pipeline which this material uses to render. If no pipeline should be given to the material a default pipeline will be used.

### Proposal

The introduction of a shader and a pipeline section in order after texture loading.

![proposal-03-1.png](proposal-03-1.png)

## Pros and Cons

### Pros

### Cons

## Conclusion

## Recommendations

## Status

Status: RFC

### Implementation details
