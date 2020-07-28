# Criticality Level

## Description

This level system should give an easy overlook on how performance critical a system is.
It consists of 4 Levels:

## Level 0

Systems with this level are not executed often and is not being depended on by just a view other systems. Here the could should be as clear as possible without any regard on performance.

### Restrictions

None

### Encouragement

It is encouraged to use a suitable high level language (such as python) to cut down development time. This code should be as clear as possible. It is encouraged to use abstractions on this level of criticality.

### Examples

An example would be a dependency script, which is only executed to setup the environment or to update it.

## Level 1

Level 1 Systems are executed occasionally and are not in critical paths.

### Restrictions

This should not be written in a high level language. High abstractions such as code generation should be avoided.

### Encouragement

This code should be as clear as possible. It is encouraged to use abstractions on this level of criticality. Lambdas and templates are encouraged to express clear intent.

### Examples

An example would be a Button press on a UI.

## Level 2

Level 2 Systems are performance dependent. Hence they should not bottleneck any surrounding systems or user interaction. Those systems are normally being depended on by other systems on regular basis.

### Restrictions

Higher abstractions such as OOP or Code generation are disallowed. Cache unfriendly container are discouraged on this level. template usage and lambdas are allowed but should be used carefully.

### Encouraged

Boilerplate should still be automated with regard to performance. Cache friendly container usage. Pre-Reservation of memory and fast general designs. Makros are encouraged.

### Example

A Resource system, it need to be executed often if a designer wants to view his changes.

## Level 3

### Restrictions

Higher abstractions such as OOP or Code generation are disallowed. Cache unfriendly container are disallowed. Lambdas are disallowed. Template usage is discouraged.

### Encouraged

Low-Level/Low-Overhead design should be used. Cache friendly container usage. Pre-Reservation of memory and fast general designs.

### Examples

The realtime user input system or the render system.
