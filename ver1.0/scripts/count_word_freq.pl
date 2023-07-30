#!/usr/bin/env perl

# print word frequency for each unique words in the file
# Thura Aung
# usage: perl count_word_freq.pl <input-file>
# Ref : https://stackoverflow.com/questions/26772009/print-word-frequencies-in-a-text-file-perl

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $wcnt = 0;
my %count;

while( my $line = <$inputFILE> ) {

    my @words = split(/\s+/, $line);
    $wcnt += scalar(@words);

    foreach my $word (@words) {
        $count{$word}++;
    }
}

foreach my $word (sort keys %count) {
    print "$word: $count{$word}\n";
}

close ($inputFILE);
