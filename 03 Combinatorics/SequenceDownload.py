from Bio import ExPASy, SeqIO

sid = raw_input("Sequence id? ")

try:
    handle = ExPASy.get_sprot_raw(sid)
    seq = SeqIO.read(handle, "swiss")
    SeqIO.write(seq, sid + ".genbank", "genbank")
    print "Sequence length", len(seq)
except Exception:
    print "Sequence not found"