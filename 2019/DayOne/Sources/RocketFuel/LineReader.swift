import Foundation

@available(macOS 10.15.4, *)
public class LineReader: Sequence {
  let encoding: String.Encoding
  let chunkSize: Int
  let delimiterData: Data
  var handle: FileHandle
  var buffer: Data
  var atEndOfFile: Bool = false

  public init(handle: FileHandle, lineDelimiterData delimiterData: Data, encoding: String.Encoding = .utf8, chunkSize: Int = 4096) {
    self.handle = handle
    self.delimiterData = delimiterData
    self.encoding = encoding
    self.chunkSize = chunkSize
    self.buffer = Data(capacity: chunkSize)
  }

  deinit {
     self.close()
  }

  public func nextLine() -> String? {
    while !atEndOfFile {
      if let delimiterRange = buffer.range(of: delimiterData) {
        let lineData = buffer.subdata(in: 0..<delimiterRange.lowerBound)
        guard let line = String(data: lineData, encoding: encoding) else {
          return nil
        }
        buffer.removeSubrange(0..<delimiterRange.upperBound)
        return line
      }

      if let nextChunk = try? handle.read(upToCount: chunkSize), !nextChunk.isEmpty {
        buffer.append(nextChunk)
      } else {
        atEndOfFile = true
        if !buffer.isEmpty {
          guard let line = String(data: buffer, encoding: encoding) else {
            return nil
          }
          return line
        }
      }
    }
    return nil
  }

  public func rewind() throws {
    try handle.seek(toOffset: 0)
    buffer.count = 0
    atEndOfFile = false
  }

  func close() {
    do {
      try handle.close()
    } catch {
      print("Failed to close file: \(handle)")
    }
  }

  public func makeIterator() -> AnyIterator<String> {
    return AnyIterator {
      return self.nextLine()
    }
  }
}
